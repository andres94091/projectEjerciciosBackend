from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)
        
    from modules.pacientes import bp as bppacientes
    from modules.datos_ejercicios import bp as bpdatos

    app.register_blueprint(bppacientes)
    app.register_blueprint(bpdatos)

    return app
