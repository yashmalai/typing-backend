from flask import send_file, jsonify
from werkzeug.utils import secure_filename
from app.extension import db
import time
import random
import string
import os
from app.config import Config

class FileController():
    model = None

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg'}

    @staticmethod
    def generate_unique_filename():
        current_time = int(time.time())
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        generated_name = f'{current_time}_{random_string}'
        return generated_name

    @classmethod
    def upload(cls, **kwargs):
        posted_file = kwargs.get("file")

        if posted_file and FileController.allowed_file(posted_file.filename):
            unique = FileController.generate_unique_filename()
            filename = secure_filename(posted_file.filename)
            file_extension = filename.rsplit('.', 1)[1]
            file_url = f"http://{Config.BASE_URL}/download/{unique}.{file_extension}"
            posted_file.save(os.path.join(f'app/{Config.UPLOAD_FOLDER}', filename))
        else:
            return jsonify({'message': 'Некорректное название файла'}), 402

        kwargs["url"] = file_url
        instance = cls.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return jsonify({"message": "File saved successfully", "id": instance.id}), 201
    
    @classmethod
    def get_file_url(cls, file_id): 
        instance = cls.model.get_or_404(file_id)
        return jsonify({"url": instance.url}), 200
    
    @classmethod
    def download(cls, filename):
        return send_file(
            os.path.join(Config.UPLOAD_FOLDER, filename),
            as_attachment=False,  # True для скачивания вместо показа
            conditional=True
        )