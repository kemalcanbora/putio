from chalice import Response


def HTTPException(status_code: int, body: str):
    return Response(body=dict(status=False,
                              description=body),
                    headers={'Content-Type': 'application/json'},
                    status_code=status_code)
