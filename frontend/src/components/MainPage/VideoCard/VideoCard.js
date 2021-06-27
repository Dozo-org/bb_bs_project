import './VideoCard.css'

function VideoCard(props) {

  const movie = props.movies
  return (
    <>
      <article className='block-video'>
        <iframe className='block-video__iframe' title="This is a unique title"></iframe>
        <h2 className='block-video__title'>{movie.title}</h2>
        <p className='block-video__caption'>{movie.info}</p>
        <a href={movie.link} className='block-video__category'>
          смотреть трейлер
        </a>
        <div className='block-video__caption block-video__caption_type_overflow'>
          <a href='/#' key={movie.tags[0].id} className='block-video__category block-video__category_type_overflow-video'>
            {movie.tags[0].name}
          </a>
          <a href='/#' key={movie.tags[1].id} className='block-video__category block-video__category_type_overflow-video'>
          {movie.tags[1].name}
          </a>
        </div>
      </article>
    </>
  );
}

export default VideoCard;
