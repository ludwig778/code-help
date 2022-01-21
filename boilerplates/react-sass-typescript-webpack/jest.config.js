module.exports = {
  verbose: true,
  setupFilesAfterEnv: ["./src/tests/setup.tsx"],
  moduleFileExtensions: ["tsx", "ts", "js"],
  testMatch: [
    "**/__tests__/*.test.(js|jsx|ts|tsx)",
  ],
  testEnvironment: "jsdom",
  moduleDirectories: ["node_modules", "src"],
  transform: {
    "\\.(ts|tsx)$": "ts-jest",
    "\\.(js|jsx)$": "babel-jest",
  }
};
