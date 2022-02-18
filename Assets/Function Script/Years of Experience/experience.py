import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # The result will be a "values" bag
    result = {
        "values": []
    }
    statuscode = 200

    # Accepted values for Years of Experience
    years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]

    try:
        values = req.get_json().get('values')
        logging.info(values)

        for rec in values:
            # Construct the basic JSON response for this record
            val = {
                    "recordId": rec['recordId'],
                    "data": {
                        "text":None
                    },
                    "errors": None,
                    "warnings": None
                }
            try:
                # Get the text to be processed from the input record
                text = rec['data']['text']
                
                # Find years
                text = ' '.join(y for y in text.split() if y in years)

                text = text.split() # Seperate years
                text = set(text)    # Remove duplicates
                text = list(text)   # Convert to list
                text.sort()         # Sort list ascending 

                # Get Years of Experience 
                temp_len = len(text)
                if temp_len != 0:
                    yoe_low = int(text[0])
                    yoe_high = int(text[temp_len-1])
                    YearsOfExp = yoe_high - yoe_low
                else:
                    YearsOfExp = None

                if YearsOfExp is None:
                    text = "Not Available"
                else:
                    text = f"{YearsOfExp} year(s)"

                # Store the cleaned text
                val["data"]["text"] = text
            except:
                # An error occured for this text record, so add lists of errors and warning
                val["errors"] =[{"message": "An error occurred processing the text."}]
                val["warnings"] = [{"message": "One or more inputs failed to process."}]
            finally:
                # Add the value for this record to the response
                result["values"].append(val)
    except Exception as ex:
        statuscode = 500
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