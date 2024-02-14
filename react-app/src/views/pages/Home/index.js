import { useDispatch, useSelector } from "react-redux";

import { Box } from "@mui/system";
import { useEffect } from "react";

import {
  getBrandsAction,
  getVehiclesAction,
} from "../../../redux/actions/VehicleActions";

import VehicleCard from "./VehicleCard";
import CustomContainer from "../../components/CustomContainer";
import SearchVehicle from "./SearchVehicle";

function Home() {
  const vehicleStore = useSelector((state) => state.vehicleStore);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getVehiclesAction);
    dispatch(getBrandsAction);
  }, []);

  return (
    <CustomContainer>
      <Box
        sx={{
          backgroundColor: "#362b358c",
          border: "2px solid purple",
          color: "white",

          "& label": {
            color: "#ffb7ff",
          },

          "& .MuiInputBase-input": {
            color: "white",
          },
          "& p": {
            color: "#ffb7ff",
          },
        }}
      >
        <SearchVehicle />
      </Box>

      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",
          "& > *": {
            m: 1,
            width: "30%",
          },
        }}
      >
        {vehicleStore?.data?.map((vehicle, ind) => {
          return <VehicleCard key={ind} vehicle={vehicle} />;
        })}
      </Box>
    </CustomContainer>
  );
}

export default Home;
