// (c) 2012 Dalek Labs

/**
 * App
 */
$(function() {

  var template = new Template($('#results'), 'template_documents');

  var queryHandler = new QueryHandler('/query', function(data) {
    template.refresh(data);
  });

  var actionHandler = new ActionHandler('/action', function() {
    setTimeout(function() {
      queryHandler.query();      
    }, 500); // Wait for update.
  });

  var queryForm = new QueryForm($('#query'), queryHandler);
  var actionForm = new ActionForm($('#action'), actionHandler);

  queryHandler.query();

  console.log('ok');
})

/**
 * Query Handler.
 */
QueryHandler = function(url, callback) {
  var self = this;
  
  self._url = url;
  self._callback = callback;
}

QueryHandler.prototype.query = function() {
  var self = this;

  console.log('query...');
  $.ajax({
    url: self._url,
  }).done(function(data) {
    self._callback(data);
    console.log(data);
  });
};

/**
 * Action Handler.
 */
ActionHandler = function(url, callback) {
  var self = this;
  
  self._url = url;
  self._callback = callback;
};

ActionHandler.prototype.insert = function(url, opt_callback) {
  var self = this;

  $.ajax({
    method: 'post',    
    url: self._url,
    data: {
      url: url
    }
  }).done(function() {
    if (opt_callback) {
      opt_callback();
    }
    self._callback();
    console.log('ok');    
  });  
};

/**
 *
 */
QueryForm = function(button, handler) {
  var self = this;

  button.click(function(event) {
    handler.query();
  });  
};

/**
 *
 */
ActionForm = function(form, handler) {
  var self = this;
  
  form.submit(function(event) {
    var input = $(event.target['url']);
    var url = input.val();
    if (!url || !Util.validateURL(url)) {
      input.focus();
    } else {
      handler.insert(url, function() {
        form[0].reset();
      });        
    }

    return false; // Prevent submit.
  })
};

/**
 * Template wrapper.
 */  
Template = function(container, id) {
  var self = this;

  self._container = container;
  self._template = jstGetTemplate(id);
};

Template.prototype.refresh = function(data) {
  var self = this;

  self._container.empty().append(self._template);
  jstProcess(new JsEvalContext(data), self._template);
};

/**
 * Utils.
 */
Util = function() {}

Util.format = function(date, c) {
  var iso = new Date(date).toISOString();
  return iso.slice(0, 10) + " " + iso.slice(11, 19);
};

Util.URL_REGEX = /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)/;

Util.validateURL = function(url) {
  return Util.URL_REGEX.test(url);
};
