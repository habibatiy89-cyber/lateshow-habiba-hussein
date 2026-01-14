from flask import Blueprint, request, jsonify
from server.models import Show
from server.extensions import db

shows_bp = Blueprint("shows", __name__)

# GET all shows
@shows_bp.route("/", methods=["GET"])
def get_shows():
    shows = Show.query.all()
    data = [{"id": s.id, "title": s.title, "date": s.date, "location": s.location} for s in shows]
    return jsonify(data), 200

# GET single show by id
@shows_bp.route("/<int:id>", methods=["GET"])
def get_show(id):
    show = Show.query.get(id)
    if not show:
        return jsonify({"error": "Show not found"}), 404
    return jsonify({"id": show.id, "title": show.title, "date": show.date, "location": show.location}), 200

# POST a new show
@shows_bp.route("/", methods=["POST"])
def create_show():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    new_show = Show(
        title=data["title"],
        date=data.get("date"),
        location=data.get("location")
    )
    db.session.add(new_show)
    db.session.commit()
    return jsonify({"id": new_show.id, "title": new_show.title, "date": new_show.date, "location": new_show.location}), 201

# PUT / Update a show
@shows_bp.route("/<int:id>", methods=["PUT"])
def update_show(id):
    show = Show.query.get(id)
    if not show:
        return jsonify({"error": "Show not found"}), 404

    data = request.get_json()
    show.title = data.get("title", show.title)
    show.date = data.get("date", show.date)
    show.location = data.get("location", show.location)

    db.session.commit()
    return jsonify({"id": show.id, "title": show.title, "date": show.date, "location": show.location}), 200

# DELETE a show
@shows_bp.route("/<int:id>", methods=["DELETE"])
def delete_show(id):
    show = Show.query.get(id)
    if not show:
        return jsonify({"error": "Show not found"}), 404

    db.session.delete(show)
    db.session.commit()
    return jsonify({"message": f"Show {id} deleted"}), 200
