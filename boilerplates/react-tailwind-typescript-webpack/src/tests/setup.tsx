import "regenerator-runtime/runtime";
import "runtime-config";
import "@testing-library/jest-dom";
import { mockServer } from "tests/utils";

beforeAll(() => mockServer.listen());
afterEach(() => mockServer.resetHandlers());
afterEach(() => localStorage.clear());
afterAll(() => {
  jest.clearAllMocks();

  mockServer.close();
});

jest.setTimeout(10000);
