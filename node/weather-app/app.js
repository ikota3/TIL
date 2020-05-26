const yargs = require("yargs");
const geocode = require("./utils/geocode");
const forecast = require("./utils/forecast");

/**
 * Fetch weather data from address.
 *
 * @param {string} address
 */
function fetchWeatherData(address) {
  geocode(address, (error, { latitude, longitude, location } = {}) => {
    if (error) {
      return console.log(error);
    }
    console.log(latitude, longitude, location);

    forecast(
      latitude,
      longitude,
      (error, { weather_description, temperature, feelslike }) => {
        if (error) {
          return console.log(error);
        }
        console.log(
          `${weather_description}. It is currently ${temperature} degrees out. It feels like ${feelslike} degrees out.`
        );
      }
    );
  });
}

// weather command
// usage: node app.js weather --address="Tokyo"
yargs.command({
  command: "weather",
  describe: "Show weather data from address.",
  builder: {
    address: {
      describe: "address.",
      demandOption: true,
      type: "string",
    },
  },
  handler({ address }) {
    fetchWeatherData(address);
  },
});

yargs.parse();
