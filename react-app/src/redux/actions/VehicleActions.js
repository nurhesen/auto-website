const axios = require("axios").default;

export const getVehiclesAction = (dispatch, getState) => {
  const { searchForm } = getState();

  dispatch({
    type: "GET_VEHICLE_REQUEST",
  });
  axios
    .get(process.env.REACT_APP_API_URL + "/vehicles/", {
      params: Object.fromEntries(
        Object.entries(searchForm).filter(([_, v]) => v != "")
      ),
    })
    .then(function (response) {
      dispatch({
        type: "GET_VEHICLE_LIST_SUCCESS",
        payload: response.data,
      });
    })
    .catch(function (error) {
      dispatch({
        type: "GET_VEHICLE_ERROR",
      });
    });
};

export const getCurrentVehicleAction = (id) => async (dispatch, getState) => {
  const { searchForm } = getState();

  dispatch({
    type: "GET_VEHICLE_REQUEST",
  });
  axios
    .get(process.env.REACT_APP_API_URL + "/vehicles/" + id + "/", {
      params: Object.fromEntries(
        Object.entries(searchForm).filter(([_, v]) => v != "")
      ),
    })
    .then(function (response) {
      dispatch({
        type: "GET_CURRENT_VEHICLE_SUCCESS",
        payload: response.data,
      });
    })
    .catch(function (error) {
      dispatch({
        type: "GET_VEHICLE_ERROR",
      });
    });
};

export const getBrandsAction = (dispatch) => {
  dispatch({
    type: "GET_BRAND_LIST_REQUEST",
  });
  axios
    .get(process.env.REACT_APP_API_URL + "/vehicles/brands/")
    .then(function (response) {
      dispatch({
        type: "GET_BRAND_LIST_SUCCESS",
        payload: response.data.brands,
      });
    })
    .catch(function (error) {
      dispatch({
        type: "GET_BRAND_LIST_ERROR",
      });
    });
};
export const searchFormChange = (args) => async (dispatch) => {
  dispatch({
    type: "STORE_SEARCH_FORM",
    payload: args,
  });
};
