import "./Question.css";
import React from "react";

function Question(props) {
  const tagNames = [];
  props.questionData.tags.forEach((tag) => {
    tagNames.push(tag.name);
  });

  const [answerVisible, setAnswerVisible] = React.useState(false);

  const handleAnswerButtonClick = () => {
    setAnswerVisible(!answerVisible);
  };

  return (
    <article className="question background-white">
      <h2 className="question__title">
        {props.questionData.title}
        <button
          type="button"
          className={`question__button ${
            answerVisible ? "question__button_active" : ""
          }`}
          onClick={handleAnswerButtonClick}
        />
      </h2>
      <span className="question__category">{tagNames}</span>
      <p
        className={`question__answer ${
          answerVisible ? "question__answer_visible" : ""
        }`}
      >
        {props.questionData.answer}
      </p>
    </article>
  );
}

export default Question;
