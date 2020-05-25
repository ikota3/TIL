const request = require("postman-request");

const geocode = (address, callback) => {
  const accessKey = "";
  const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(
    address
  )}.json?access_token=${accessKey}&limit=1`;

  request({ url: url, json: true }, (error, response, body) => {
    if (error) {
      callback("Unable to connect to mapbox.", undefined);
      return;
    }
    if (body.features.length === 0) {
      callback("Unable to find location. Try another search.", undefined);
      return;
    }
    const feature = body.features[0];
    callback(undefined, {
      latitude: feature.center[1],
      longitude: feature.center[0],
      location: feature.place_name,
    });
  });
};

module.exports = { geocode };

console.log(module.exports);
