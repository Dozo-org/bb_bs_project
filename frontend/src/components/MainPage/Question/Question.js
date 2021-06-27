import './Question.css';

function Question(props) {
  return (
    <section className='three-columns'>
      <article className='block-questions background-white'>
        <h2 className='block-questions__title'>
         {props.question.title}
        </h2>
        <a href='/#' className='block-questions__category'>
          {props.question.tags[0].name}
        </a>
      </article>
    </section>
  );
}

export default Question;
