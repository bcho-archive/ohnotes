var app = app || {};

(function() {
    'use strict';

    app.Note = Backbone.Model.extend({
        defaults: {
            'id': 0,
            'name': '',
            'content': null
        },

        /* get content */
        url: function() {
            return app.basic_url + '/notes/' + this.id;
        }
    });

    app.Query = Backbone.Model.extend({
        defaults: {
            'word': null,
            'ids': []
        },

        url: function() {
            return app.basic_url + '/query/word/' + this.get('word');
        },

        parse: function(resp) {
            var ids = [];
            _.each(resp, function(o) { ids.push(o.id); }, this);
            return {'ids': ids};
        },

        /* show all notes and reset the state */
        reset: function() {
            var ids = [];
            _.each(app.notes.models, function(o) { ids.push(o.get('id')); }, this);
            this.set('ids', ids);
            this.set('word', null);
        }
    });
}());
