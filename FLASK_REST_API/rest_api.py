from flask import Flask
from flask_restful import Resource, Api, reqparse, request, abort
import json

app = Flask("VideoAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("title", required=True)
parser.add_argument("uploadDate", type=int, required=False)

"""
videos = {
    "video1": {"title": "Hello World in python", "uploadDate": 20210917},
    "video2": {"title": "Why language something", "uploadDate": 20210918},
}
"""

with open("videos.json", "r") as f:
    videos = json.load(f)


def write_changes_to_file():
    global videos
    videos = {
        k: v
        for k, v in sorted(videos.items(), key=lambda videos: videos[1]["uploadDate"])
    }
    with open("videos.json", "w") as f:
        json.dump(videos, f)


# write_changes_to_file()


class Video(Resource):
    def get(self, video_id):
        if video_id == "all":
            return videos
        if video_id not in videos:
            abort(404, message=f"Video {video_id} not found!")
        return videos[video_id]

    def put(self, video_id):
        title = request.form.get("title")
        uploadDate = request.form.get("uploadDate")

        if title is None:
            data = request.get_json(silent=True) or {}
            title = data.get("title")

        if not title:
            return {"message": "Missing field: title"}, 400

        if uploadDate is None:
            data = request.get_json(silent=True) or {}
            title = data.get("uploadDate")
        if uploadDate is not None:
            uploadDate = int(uploadDate)

        videos[video_id] = {"title": title, "uploadDate": uploadDate}
        write_changes_to_file()
        return {video_id: videos[video_id]}, 201

    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f"Video {video_id} not found!")
        del videos[video_id]
        write_changes_to_file()
        return "", 204


class VideoSchedule(Resource):

    def get(self):
        return videos, 200

    def post(self):
        title = request.form.get("title")
        uploadDate = request.form.get("uploadDate")
        if title is None:
            data = request.get_json(silent=True) or {}
            title = data.get("title")

        if not title:
            return {"message": "Missing field: title"}, 400

        if uploadDate is None:
            data = request.get_json(silent=True) or {}
            title = data.get("uploadDate")
        if uploadDate is not None:
            uploadDate = int(uploadDate)

        # Taking all the individual video_ids we have and stripping away the video string
        #   This leads us to have numbers left, int(num) -> list(num) -> max(num) + 1 -> next_video_id
        video_id = max(int(v.lstrip("video")) for v in videos.keys()) + 1

        video_id = f"video{video_id}"

        videos[video_id] = {"title": title, "uploadDate": uploadDate}
        write_changes_to_file()
        return {video_id: videos[video_id]}, 201


api.add_resource(Video, "/videos/<video_id>")
api.add_resource(VideoSchedule, "/videos")

# IPv6 is tried before IPv4, so we need to explicitly:
#   curl -4 http://localhost:5000/
if __name__ == "__main__":
    app.run()
