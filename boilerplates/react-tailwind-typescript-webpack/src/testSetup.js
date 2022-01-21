import "runtime-config";
import "regenerator-runtime/runtime";
import "@testing-library/jest-dom";
import React from "react";
import { act, render } from "@testing-library/react";
import { Provider } from "react-redux";
import { generateStore } from "reducers";
import { rest } from "msw";
import { setupServer } from "msw/node";

const mockResponse = (method, path, status, data = {}) => {
  return rest[method](path, (_, res, ctx) =>
    res(ctx.status(status), ctx.json(data))
  );
};

const server = setupServer();
global.mockServer = server;
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterEach(() => localStorage.clear());
afterAll(() => {
  jest.clearAllMocks();

  server.close();
});

const sleep = async (ms) => {
  await new Promise((r) => setTimeout(r, ms));
};

const actSleep = async (ms) => {
  await act(async () => {
    await sleep(ms);
  });
};

const renderWithProvider = (ui, store = null) => {
  if (!store) {
    store = generateStore();
  }

  render(ui, {
    wrapper: ({ children }) => <Provider store={store}>{children}</Provider>,
  });

  return store;
};

global.React = React;
global.sleep = sleep;
global.actSleep = actSleep;
global.renderWithProvider = renderWithProvider;
global.generateStore = generateStore;
global.mockResponse = mockResponse;
