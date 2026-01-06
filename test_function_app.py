# test_function_app.py

import json
import azure.functions as func

from function_app import http_trigger  # your code module


def test_http_trigger_with_name_query():
    # Arrange: build an HttpRequest with ?name=Kourosh
    req = func.HttpRequest(
        method="GET",
        url="/api/http_trigger",
        params={"name": "Kourosh"},
        body=None,
    )

    # Act
    resp = http_trigger(req)

    # Assert
    assert isinstance(resp, func.HttpResponse)
    assert resp.status_code == 200
    assert resp.get_body().decode() == (
        "Hello, Kourosh. This HTTP triggered function executed successfully."
    )


def test_http_trigger_with_name_body():
    # Arrange: no query param, name in JSON body
    body = json.dumps({"name": "Kourosh"}).encode("utf-8")
    req = func.HttpRequest(
        method="POST",
        url="/api/http_trigger",
        params={},  # empty query
        body=body,
    )

    # Act
    resp = http_trigger(req)

    # Assert
    assert resp.status_code == 200
    assert resp.get_body().decode() == (
        "Hello, Kourosh. This HTTP triggered function executed successfully."
    )


def test_http_trigger_without_name():
    # Arrange: no query param, empty body
    req = func.HttpRequest(
        method="GET",
        url="/api/http_trigger",
        params={},
        body=b"",
    )

    # Act
    resp = http_trigger(req)

    # Assert
    assert resp.status_code == 200
    assert "Pass a name in the query string" in resp.get_body().decode()
