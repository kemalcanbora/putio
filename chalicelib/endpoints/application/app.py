from chalice import Blueprint
from chalicelib.core.app import PutIo
from io import BytesIO
from uuid import uuid4
import cgi

application = Blueprint(__name__)


@application.route('/upload', methods=['PUT'], content_types=["multipart/form-data"])
def upload():
    body = application.current_request.raw_body
    content_type = application.current_request.headers['content-type']
    _, parameters = cgi.parse_header(content_type)
    parameters['boundary'] = parameters['boundary'].encode('utf-8')

    rfile = BytesIO(application.current_request.raw_body)

    parsed = cgi.parse_multipart(rfile, parameters).get("name", None)
    if parsed is None:
        file_name = uuid4().__str__()
    else:
        file_name = parsed[0]

    PutIo().upload(filename=file_name, data=body)
    return {"status": True}


@application.route('/list', methods=['GET'])
def list_files():
    return PutIo().list()


@application.route('/download/{doc_id}', methods=['GET'])
def download(doc_id):
    return PutIo().download(doc_id=doc_id)
