const geocode = require("./utils/geocode");

const weatherKey = "";
const weatherQuery = "37.8267,-122.4233";
const weatherUrl = `http://api.weatherstack.com/current?access_key=${weatherKey}&query=${weatherQuery}&units=m`;

geocode.geocode("Fukuoka", (error, data) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(data);
});

// request({ url: weather_url, json: true }, (error, response, body) => {
//   if (error) {
//     console.log("Unable to connect weather stack.");
//     return;
//   }
//   if (body.error) {
//     console.log("Unable to find location.");
//     return;
//   }
//   const currentData = body.current;
//   console.log(
//     `${currentData.weather_descriptions[0]}. It is currently ${currentData.temperature} degrees out. It feels like ${currentData.feelslike} degrees out.`
//   );
// });
