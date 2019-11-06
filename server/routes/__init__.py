def init_route(app):
    from .image import image_bp
    from .record import record_bp

    app.register_blueprint(image_bp)
    app.register_blueprint(record_bp)