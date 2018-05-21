"""Utils for requests in flask."""

import json as _json
from flask import request as _request, make_response as _make_response

from {{cookiecutter.package_name}}_flask import app


def json_request(api_name, request_type, encoding='utf-8'):
    """Json Request.

    Parameters:
    ----------
    api_name : string
        Name of the api.
    request_type : string
        POST or GET.

    """
    try:
        request_text = _request.data
        json_object = _json.loads(request_text.decode(encoding))
        app.logger.info(
            "Request for '%s/%s': %s",
            api_name, request_type, _json.dumps(json_object, indent=2)
        )
    except Exception as err:
        app.logger.error(
            "Unable to parse the given text: %s in %s/%s",
            request_text, api_name, request_type
        )
        return None, err
    return json_object, None


def json_response(json_object, api_name, request_type, status_code=200):
    """Create a rest response of content-type application/json.

    Parameters:
    ----------
    json_object : dict|list
        Response json object.
    api_name: string
        Name of the api.
    request_type: string
        Type of the request.
    status_code : int
        (the default is 200)

    Returns
    -------
    flask.Response

    """
    json_string = _json.dumps(json_object, indent=2)
    app.logger.info(
        "Response from '%s/%s': %s",
        api_name, request_type, json_string
    )
    response = _make_response(json_string)
    response.headers['content-type'] = "application/json"
    response.status_code = status_code
    return response


def text_response(response_text, api_name, request_type, status_code=200):
    """Create a rest response of content-type text/plain.

    Parameters:
    ----------
    response_text : string
        Response text.
    api_name: string
        Name of the api.
    request_type: string
        Type of the request.
    status_code : integer, optional
        (the default is 200)

    Returns
    -------
    flask.Response

    """
    app.logger.info(
        "Response from '%s/%s': '%s'",
        api_name, request_type, response_text
    )
    response = _make_response(response_text)
    response.headers['content-type'] = "text/plain"
    response.status_code = status_code
    return response
