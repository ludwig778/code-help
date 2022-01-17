import * as React from "react";
import { act, render } from "@testing-library/react";
import { Provider } from "react-redux";
import { Store } from "redux";
//import { generateStore } from "reducers/root";
import { rest } from "msw";
import { SetupServerApi, setupServer } from "msw/node";

export const mockServer: SetupServerApi = setupServer();

export const mockResponse = (method, path, status, data = {}) => {
  return rest[method](path, (_, res, ctx) =>
    res(ctx.status(status), ctx.json(data))
  );
};

export const sleep = async (ms: number): Promise<void> => {
  await new Promise((r) => setTimeout(r, ms));
};

export const actSleep = async (ms: number): Promise<void> => {
  await act(async () => {
    await sleep(ms);
  });
};

export const renderWithProvider = (ui: JSX.Element, store = null): Store => {
  //if (!store) {
  //  store = generateStore();
  //}

  render(ui, {
    wrapper: ({ children }) => <Provider store={store}>{children}</Provider>,
  });

  return store;
};
