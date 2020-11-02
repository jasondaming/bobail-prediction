from app import create_app
import ptvsd

ptvsd.enable_attach(address=("0.0.0.0", 5678))
ptvsd.wait_for_attach()

app = create_app()