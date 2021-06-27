import React from 'react';
import { Link } from 'react-router-dom';
import CalendarBlock from '../../CalendarBlock/CalendarBlock';
import Article from '../Article/Article';
import ArticleBlock from '../ArticleBlock/ArticleBlock';
import VideoCard from '../VideoCard/VideoCard';
import Question from '../Question/Question';
import api from '../../../utils/api';
import Loader from '../../Loader/Loader';
import './Main.css';


function Main(props) {
 
  const [mainPageContent, setMainPageContent] = React.useState({});
  const [isContentReady, setIsContentReady] = React.useState(false);

  React.useEffect(() => {
    api.getMainPage().then(res => {
      setMainPageContent(res.data)
      setIsContentReady(true)
    })

  }, [])
  
  if (isContentReady) {
    return   (
      <>
        <section className="two-columns two-columns_style_first">
          { props.isLoggedIn ? 
            <CalendarBlock 
              event={mainPageContent.event} 
              enroll={props.enroll}
              mainPage={true}
            /> 
            : <Article /> 
          }
          <Link to="#" className="link">
            <article className="block-photo">
              <h2 className="block-photo__title">{mainPageContent.history.title}</h2>
            </article>
          </Link>
        </section>
        <section className="two-columns two-columns_style_place ">
          <article className="block-place background-yellow">
            <p className="block-place__tag">выбор наставника</p>
            <h2 className="block-place__title">{mainPageContent.place.title}</h2>
            <p className="block-place__caption">{mainPageContent.place.name}</p>
            <div className="block-place__image"></div>
            <a href={mainPageContent.place.link} className="block-place__category">перейти на сайт</a>
          </article>
          <article className="block-place_type_description background-white">
            <p className="block-place__caption">{mainPageContent.place.info}</p>
            <p className="block-place__text">{mainPageContent.place.description}</p>
          </article>
        </section>
        <ArticleBlock className={'background-blue'} text={mainPageContent.articles[0].title} />
        <section className='four-columns'>
          {mainPageContent.movies.map((movie, index) => (
            <VideoCard index={index} key={index} movies={movie}/>
          ))}
        </section>
        <section className="two-columns two-columns_style_video-header">
          <article className="block-video-header block-video-header_type_description background-yellow">
            <h2 className="block-video-header__title">{mainPageContent.video.title}</h2>
            <p className="block-video-header__caption">{mainPageContent.video.info}</p>
            <a href={mainPageContent.video.link} className="block-video-header__category">смотреть видео</a>
          </article>
          <article className="block-video-header">
            <iframe className="block-video-header__iframe" title="This is a unique title"/>
          </article>
        </section>
        <section className='two-columns two-columns_style_questions'>
          <article className='block-links'>
            <iframe
              className='block-links__iframe'
              title='block-links__iframe'
              src='https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Ffacebook&amp;tabs=timeline&amp;width=420&amp;height=1000&amp;small_header=false&amp;adapt_container_width=true&amp;hide_cover=false&amp;show_facepile=true&amp;appId'
              allow='autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share' 
            ></iframe>
          </article>
          <section className='three-columns'>
            {mainPageContent.questions.map(question=>(
              <Question key={question.id} question={question}/>
              ))}
          </section>
        </section>
        <ArticleBlock className={'background-green'} text={mainPageContent.articles[1].title} />
      </>
    ) 
  } 
    return <Loader />
  
   
}

export default Main;
