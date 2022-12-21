import aghpb_api
from waitress import serve
from decouple import config

if __name__ == "__main__":
    serve(aghpb_api.app, host='0.0.0.0', port=config("PORT", default=8081, cast=int))