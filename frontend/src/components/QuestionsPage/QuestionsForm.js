import "./QuestionsForm.css";

function QuestionsForm() {
  return (
    <div className="questions-form__wrapper">
      <h2 className="questions-form__title">
        Если вы не нашли ответ на свой вопрос — напишите нам, и мы включим его в
        список
      </h2>
      <form
        action="#"
        name="questions"
        className="questions-form__form"
        method="POST"
      >
        <label className="questions-form__field">
          <input
            id="questions-input"
            required
            name="question"
            minLength={2}
            maxLength={100}
            placeholder="Введите вопрос"
            className="questions-form__input"
            type="text"
          />
          <span className="questions-form__input-error" />
        </label>
        <button
          aria-label="submit form"
          className="questions-form__button-submit"
          type="submit"
        >
          Отправить
        </button>
      </form>
    </div>
  );
}

export default QuestionsForm;
