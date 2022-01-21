import React from "react";
import { render, screen } from "@testing-library/react";
import App from "app";

test("check app", () => {
  render(<App />);

  expect(screen.getByText("My App")).toBeInTheDocument();
});
