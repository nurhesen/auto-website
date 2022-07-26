import { combineReducers } from "redux";
import {
  vehicleStoreReducer,
  brandStoreReducer,
  searchFormReducer,
} from "./VehicleReducers";

export default combineReducers({
  vehicleStore: vehicleStoreReducer,
  brandStore: brandStoreReducer,
  searchForm: searchFormReducer,
});
