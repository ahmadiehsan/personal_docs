# React

## Redux devtools

install:

- chrome:

  https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd

- firefox:

  https://addons.mozilla.org/en-US/firefox/addon/reduxdevtools/

usage:

```react
// index.js

import {createStore, applyMiddleware, compose} from 'redux';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
    reducers,
    composeEnhancers(applyMiddleware())
);
```

## react-intl (i18n)

Install:

- `npm i --save react-intl`
- `npm i --save-dev react-intl-cra react-intl-po`

usage:

```react
// index.js

import {IntlProvider} from "react-intl";
import {addLocaleData} from "react-intl";
import locale_en from 'react-intl/locale-data/en';
import locale_fa from 'react-intl/locale-data/fa';

import localeData from "./translation/localeData";

// Translation (react-intl)
addLocaleData([...locale_en, ...locale_fa]);
const language = 'en-US';
const languageWithoutRegionCode = 'en';
const messages = localeData[languageWithoutRegionCode];

ReactDOM.render(
    <IntlProvider locale={language} messages={messages}>
        <App/>
    </IntlProvider>
);
```

```
// package.json

"scripts": {
	"extract:messages": "react-intl-cra 'src/**/*.js' -o 'src/translation/messages/messages.json'",
	"extract:pot": "npm run extract:messages && react-intl-po json2pot 'src/translation/messages/messages.json' -c 'id' -o 'src/translation/messages/messages.pot'",
	"extract:po": "react-intl-po po2json 'src/translation/locale/*.po' -c 'id' -m 'src/translation/messages/messages.json' -o 'src/translation/localeData.json'"
}
```

```react
// react component

import {FormattedMessage} from 'react-intl';

<FormattedMessage
	id="<unique message id: navBar.brandName>"
	defaultMessage="<message text>"
/>
```

Create .po and final json file:
1. `npm run extract:pot`
2. create `src/translation/locale/` directory
3. use .pot file in `src/translation/messages/messages.pot` for creating fa.po and en.po
4. move fa.po and en.po to `src/translation/locale/`
5. `npm run extract:po`

## date picker

install: `npm install react-persian-datepicker --save`

usage:

- in redux form

  ```react
  import {DatePicker} from 'react-persian-datepicker';
  
  export const datePicker = ({input: {name, onBlur, onChange, onDragStart, onDrop, onFocus, value}}) => {
      const styles = {
          calendarContainer: "calendarContainer",
          dayPickerContainer: "dayPickerContainer",
          monthsList: "monthsList",
          daysOfWeek: "daysOfWeek",
          dayWrapper: "dayWrapper",
          selected: "selected",
          heading: "heading",
          next: "next",
          prev: "prev",
          title: "title",
          currentMonth: "currentMonth"
      };
  
  return (
      <DatePicker
          onChange={onChange}
          onFocus={onFocus}
          onBlur={onBlur}
          calendarStyles={styles}
          className="form-control"
      />
  );
  
  };
  ```

- in react

  ```react
  import {DatePicker} from 'react-persian-datepicker';
  
  class DatePicker extends React.Component {
  	render() {
          const styles = {
              calendarContainer: "calendarContainer",
              dayPickerContainer: "dayPickerContainer",
              monthsList: "monthsList",
              daysOfWeek: "daysOfWeek",
              dayWrapper: "dayWrapper",
              selected: "selected",
              heading: "heading",
              next: "next",
              prev: "prev",
              title: "title",
              currentMonth:"currentMonth"
          };
  
      return (
          <DatePicker calendarStyles={styles}/>
      );
  }
  
  }
  ```
