=======
Falcon
=======

Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST APIs and micro services, with a focus on reliability, correctness, and performance at scale.

- OpenStack, Rackspace, Opera etc. using falcon.
- Falcon tries to do as little as possible while remaining highly effective.
  - ASGI, WSGI, and WebSocket support
  - Native asyncio support
  - Simple API modeling through centralized RESTful routing


Simple Falcon App
==================

::

    import json
    import falcon

    class ObjRequestClass:
        def on_get(self, req, resp):
            content = {
                "name": "ajeeb",
                "place": "bangalore"
            }
            resp.body = json.dumps(content)

    app = falcon.API()
    app.add_route('/test', ObjRequestClass())


Run falcon app using WSGI web servers
======================================

Using Gunicorn
---------------

Install Gunicorn in venv: `pip install gunicorn`
    
::

    $ gunicorn falcon_test:app
    [2022-09-04 10:48:22 +0530] [77099] [INFO] Starting gunicorn 20.1.0
    [2022-09-04 10:48:22 +0530] [77099] [INFO] Listening at: http://127.0.0.1:8000 (77099)
    [2022-09-04 10:48:22 +0530] [77099] [INFO] Using worker: sync
    [2022-09-04 10:48:22 +0530] [77101] [INFO] Booting worker with pid: 77101


GET API

::

    $ curl -X GET http://127.0.0.1:8000/test
    {
        "name": "ajeeb",
        "place": "bangalore"
    }

Using uWSGI
------------

TBD

