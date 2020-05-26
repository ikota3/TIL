const request = require("postman-request");

/**
 * Get forecast message from giving latitude and longitude.
 * Returns forecast message.
 *
 * @param {string} latitude
 * @param {string} longitude
 * @param {Function} callback
 */
const forecast = (latitude, longitude, callback) => {
  const accessKey = "";
  const latitudeAndLongitude = encodeURIComponent(`${latitude},${longitude}`);
  const url = `http://api.weatherstack.com/current?access_key=${accessKey}&query=${latitudeAndLongitude}&units=m`;

  request({ url, json: true }, (error, { body }) => {
    if (error) {
      callback("Unable to connect to weather stack.", undefined);
      return;
    }
    if (body.error) {
      callback("Unable to find location.", undefined);
      return;
    }
    const currentData = body.current;
    const data = {
      weather_description: currentData.weather_descriptions[0],
      temperature: currentData.temperature,
      feelslike: currentData.feelslike,
    };
    callback(undefined, data);
  });
};

module.exports = forecast;
