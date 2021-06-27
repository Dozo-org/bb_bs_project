import './AboutUs.css';


function AboutUs () {
  return (
<section className="about">
        <h1 className="about__header">
          Наставники.про – цифоровая информационная платформа огрганизации «Старшие Братья Старшие Сестры».
          Созданная для поддержки наставников программы.
        </h1>
        <a href="https://www.nastavniki.org/o-nas/ob-organizaczii/">
          <div className="about__logo" />
        </a>
        <div className="about__circle-square">
          <div className="about__circle">
            <h2 className="about__circle-title">Об организации</h2>
          </div>
          <div className="about__square">
            <p className="about__paragraph">«Старшие Братья Старшие Сестры» — межрегиональная общественная организация
              содействия воспитанию подрастающего поколения. Мы поддерживаем детей, которым требуется внимание:
              оставшихся без попечения родителей, приемных, детей из неполных, многодетных или неблагополучных семей,
              детей с ограниченными возможностями.</p>
            <p className="about__paragraph">Любому человеку, тем более ребенку, необходимо общение. Без него дети растут
              неуверенными и замкнутыми. Одиночество токсично, а самое надежное противоядие – дружба.</p>
            <p className="about__paragraph">Мы помогаем детям, которым не хватает поддержки взрослого друга, «Младшим».
              Таким другом становится наш волонтер, «Старший». Он принимает ребенка, какой он есть, поддерживает,
              помогает раскрыть потенциал, почувствовать уверенность в своих силах, узнать элементарные вещи о жизни,
              адаптироваться и полноценно участвовать в жизни общества.</p>
          </div>
        </div>
        <div className="about__accent">
          <h3 className="about__subtitle">
            Мы хотим, чтобы наставник был у каждого ребенка, который в нем нуждается
          </h3>
        </div>
        <div className="about__three-columns">
          <div className="about__column">
            <h3 className="about__column-header background-blue">Пожертвования</h3>
            <div className="about__text">
              <p className="about__column-paragraph">Деньги пойдут на оплату работы кураторов программы (профессиональные
                психологи/социальные работники),
                которые поддерживают дружбу между ребенком и наставником.</p>
              <button type="button" className="about__action">сделать пожертвование</button>
            </div>
          </div>
          <div className="about__column">
            <h3 className="about__column-header background-orange">Наствничество</h3>
            <div className="about__text">
              <p className="about__column-paragraph">Наставник «Старшие Братья Старшие Сестры» — значимый взрослый,
                который становится для ребенка старшим другом, ролевой моделью, принимает своего «Младшего» таким,
                какой он есть. «Старший» открывает для ребенка дверь в большой мир и дарит ему надежду на более
                счастливое и успешное будущее.</p>
              <button type="button" className="about__action">подробнее</button>
            </div>
          </div>
          <div className="about__column ">
            <h3 className="about__column-header background-green">Партнерство</h3>
            <div className="about__text">
              <p className="about__column-paragraph">Компании поддерживают нас не только деньгами, но и делами. Мы собрали
                все возможные способы поддержки и сотрудничества: профессиональная помощь Pro Bono, организационная
                помощь, корпоративное волонтерство, мастер-классы, лекции, учебные программы</p>
              <button type="button" className="about__action">подробнее</button>
            </div>
          </div>
        </div>
      </section>
  )
}

export default AboutUs;