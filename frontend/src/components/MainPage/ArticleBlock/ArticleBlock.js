import './ArticleBlock.css'


function ArticleBlock(props) {
  return (
    <section className='one-column'>
      <article className={`block-article ${props.className}`}>
        <p className='block-atricle__title'>{props.text}</p>
        <p className='block-article__category'>читать статью</p>
      </article>
    </section>
  );
}

export default ArticleBlock;