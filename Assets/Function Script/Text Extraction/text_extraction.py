import logging
import json
import requests
import time
from requests import post as http_post
from requests import get as http_get
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    # The result will be a "values" bag
    result = {
        "values": []
    }
    statuscode = 200

    try:
        values = req.get_json().get('values')
        logging.info(values)

        for rec in values:
            # Construct the basic JSON response for this record
            val = {
                    "recordId": rec['recordId'],
                    "data": {
                    },
                    "errors": None,
                    "warnings": None
                }
            try:
                # get the image to be processed from the input record
                document_url = rec['data']['doc_url']
                sas_token = rec['data']['doc_sas_token']
                sas_url = document_url + sas_token
                document_response = requests.get(sas_url)
                document_content = document_response.content

                # Parse Form - you may need to change your form_recognizer_url depending on where you created the service
                form_recognizer_url = "<COGNITIVE_SERVICES_ENDPOINT>"
                form_recognizer_key = "<COGNITIVE_SERVICES_KEY>"
                
                headers = {
                    # Request headers
                    'Content-Type': 'application/pdf',
                    'Ocp-Apim-Subscription-Key': form_recognizer_key,
                }

                url = form_recognizer_url + "formrecognizer/v2.1-preview.2/layout/analyze?language=en"

                resp = http_post(url = url, data = document_content, headers = headers)
                
                #extract the url for the analysis result
                form_recognizer_result_url = resp.headers['Operation-Location']
                #change the headers
                headers = {
                        'Ocp-Apim-Subscription-Key': form_recognizer_key,
                    }

                n_tries = 10
                n_try = 0
                wait_sec = 2
                while n_try < n_tries:
                    try:
                        #Since this is async we need to give forms recognizer some time to analyze
                        resp = http_get(url = form_recognizer_result_url, headers = headers)

                        status = resp.json()["status"]
                        if status == "succeeded":
                            break
                        if status == "failed":
                            break
                        # Analysis still running. Wait and retry.
                        time.sleep(wait_sec)
                        n_try += 1
                    except Exception as e:
                        logging.info(e)
                        break

                analyzeResult = resp.json()["analyzeResult"]

                words = ""

                for text in analyzeResult["readResults"]:
                    for line in text["lines"]:
                        if (len(line["text"]) > 0):
                            words += line["text"] + " " 
                
                val["data"]["text"] = words

            except Exception as ex:
                logging.info(ex)
                # An error occured for this text record, so add lists of errors and warning
                val["errors"] =[{"message": "An error occurred processing the content."}]
                val["warnings"] = [{"message": "One or more inputs failed to process."}]
            finally:
                # Add the value for this record to the response
                result["values"].append(val)
    except Exception as ex:
        statuscode = 500
        logging.info(ex)
        # A global error occurred, so return an error response
        val = {
                "recordId": None,
                "data": {
                    "text":None
                },
                "errors": [{"message": ex.args}],
                "warnings": [{"message": "The request failed to process."}]
            }
        result["values"].append(val)
    finally:
        # Return the response
        return func.HttpResponse(body=json.dumps(result), mimetype="application/json", status_code=statuscode)