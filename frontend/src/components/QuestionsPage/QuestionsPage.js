import "./QuestionsPage.css";
import React from "react";
import api from "../../utils/api";
import Question from "./Question";
import Tag from "./Tag";
import QuestionsForm from "./QuestionsForm";

function QuestionsPage() {
  const [questions, setQuestions] = React.useState([]);

  React.useEffect(() => {
    api
      .getQuestions()
      .then((data) => {
        setQuestions(data.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  const filteredQuestions = questions.map((question) => {
    return <Question questionData={question} key={question.id} />;
  });

  return (
    <>
      <section className="questions-page">
        <h1 className="title">Ответы на вопросы</h1>
        <section className="filters">
          <div className="filters__pseudo-block" />
          <ul className="filters__list">
            <Tag name="Все" />
            <Tag name="Первая встреча" />
            <Tag name="Вопросы детей" />
            <Tag name="Воспитатели / опекуны" />
            <Tag name="Сомнения" />
            <Tag name="Сложности" />
            <Tag name="Подарки" />
            <Tag name="Влияние на ребенка" />
            <Tag name="Времяпровождение" />
            <Tag name="Ответственность" />
            <Tag name="Завершение отношений" />
            <Tag name="Первая встреча" />
            <Tag name="Вопросы детей" />
            <Tag name="Первая встреча" />
            <Tag name="Вопросы детей" />
            <Tag name="Воспитатели / опекуны" />
            <Tag name="Сомнения" />
            <Tag name="Сложности" />
          </ul>
        </section>
      </section>
      <section className="block-questions">{filteredQuestions}</section>
      <section className="questions-form">
        <QuestionsForm />
      </section>
    </>
  );
}

export default QuestionsPage;
