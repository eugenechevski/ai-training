return {
  timestamp: "2023-07-31T12:00:00Z",
  location: {
    longitude: -71.123456,
    latitude: 42.345678,
  },
  vehicleCounts: {
    total: 12345,
    cars: 7890,
    trucks: 2456,
    motorcycles: 109,
    pedestrians: 201,
  },
  speedAverages: {
    overall: 65.4,
    cars: 68.8,
    trucks: 55.6,
    motorcycles: 79.2,
  },
  incidentReports: [
    {
      type: "accident",
      description:
        "Two-vehicle accident on the shoulder, no injuries reported.",
      location: {
        longitude: -71.125678,
        latitude: 42.346789,
      },
      startTime: "2023-07-31T12:15:00Z",
    },
    {
      type: "congestion",
      description: "Slow traffic due to roadwork.",
      location: {
        longitude: -71.119876,
        latitude: 42.344567,
      },
      startTime: "2023-07-31T11:45:00Z",
      endTime: "2023-07-31T12:30:00Z",
    },
  ],
  weatherConditions: {
    temperature: 25.5,
    humidity: 65,
    precipitation: 0.2,
    windSpeed: 15.8,
    windDirection: "southwest",
    condition: "partly cloudy with rain",
  },
};
