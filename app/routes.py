from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from .weather_api import get_coordinates, get_weather
from .models import SearchHistory
from . import db

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            session['last_city'] = city
            return redirect(url_for('main.weather', city=city))
    return render_template('index.html')


@bp.route('/weather')
def weather():
    city = request.args.get('city')
    if city:
        lat, lon = get_coordinates(city)
        if lat is not None and lon is not None:
            weather_data = get_weather(lat, lon)
            if weather_data:
                # Обновление или добавление записи в истории поиска
                history = SearchHistory.query.filter_by(city=city).first()
                if history:
                    history.search_count += 1
                else:
                    history = SearchHistory(city=city)
                    db.session.add(history)
                db.session.commit()

                # Форматирование данных для отображения в таблице
                hourly_data = weather_data['hourly']
                formatted_data = []
                for time, temp in zip(hourly_data['time'], hourly_data['temperature_2m']):
                    formatted_data.append({"time": time, "temperature": temp})

                return render_template('weather.html', city=city, formatted_data=formatted_data)
            else:
                return jsonify({"error": "Failed to get weather data"}), 500
        else:
            return jsonify({"error": "Failed to get coordinates"}), 500
    else:
        return jsonify({"error": "City not provided"}), 400

@bp.route('/history')
def history():
    history = SearchHistory.query.all()
    return jsonify([{"city": h.city, "search_count": h.search_count} for h in history])