import aghpb_api
from waitress import serve

if __name__ == "__main__":
    serve(aghpb_api.app, host='0.0.0.0', port=8080)