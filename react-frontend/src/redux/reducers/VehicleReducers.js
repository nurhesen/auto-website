export const vehicleStoreReducer = (state = {}, action) => {
  switch (action.type) {
    case "GET_VEHICLE_REQUEST":
      return { ...state, loading: true };
    case "GET_VEHICLE_LIST_SUCCESS":
      return {
        ...state,
        data: action.payload,
        loading: false,
        success: true,
      };

    case "GET_CURRENT_VEHICLE_SUCCESS":
      return {
        ...state,
        current: action.payload,
        loading: false,
        success: true,
      };
    case "GET_VEHICLE_ERROR":
      return { ...state, loading: false, success: false, error: true };
    default:
      return state;
  }
};
export const brandStoreReducer = (state = {}, action) => {
  switch (action.type) {
    case "GET_BRAND_LIST_REQUEST":
      return { ...state, loading: true };
    case "GET_BRAND_LIST_SUCCESS":
      return {
        ...state,
        data: action.payload,
        loading: false,
        success: true,
      };
    case "GET_BRAND_LIST_ERROR":
      return { ...state, loading: false, success: false, error: true };

    default:
      return state;
  }
};
export const searchFormReducer = (state = {}, action) => {
  switch (action.type) {
    case "STORE_SEARCH_FORM":
      return { ...state, ...action.payload };
    default:
      return state;
  }
};
