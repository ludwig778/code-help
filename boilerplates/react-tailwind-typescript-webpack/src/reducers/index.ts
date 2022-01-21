//import { createStore, combineReducers, applyMiddleware } from "redux";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

//const rootReducer = combineReducers({});
const rootReducer = (state) => state;

export function generateStore(initialState = {}) {
  return createStore(rootReducer, initialState, applyMiddleware(thunk));
}

export const store = generateStore();
