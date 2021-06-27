import { useEffect } from "react";
import Lottie from "lottie-web";

function Animation({ animationData }) {
  useEffect(() => {
    const container = document.querySelector(".not-found__animation");
    const options = {
      container,
      animationData,
    }
    Lottie.loadAnimation(options);
  }, [animationData]);
  return <div className="not-found__animation" />;
}

export default Animation;
