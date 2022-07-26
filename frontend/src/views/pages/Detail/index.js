import { useDispatch, useSelector } from "react-redux";

import { useEffect } from "react";

import { useParams } from "react-router-dom";
import VehicleDetail from "./VehicleDetail";

import { getCurrentVehicleAction } from "../../../redux/actions/VehicleActions";
import CustomContainer from "../../components/CustomContainer";
function Detail() {
  const vehicleStore = useSelector((state) => state.vehicleStore);

  const params = useParams();
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCurrentVehicleAction(params.id));
  }, []);

  return (
    <CustomContainer>
      <VehicleDetail current={vehicleStore?.current} />
    </CustomContainer>
  );
}

export default Detail;
