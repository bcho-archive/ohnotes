var app = app || {};

(function() {
    'use strict';

    var Notes = Backbone.Collection.extend({
        model: app.Note,
        /* get notes list */
        url: app.basic_url + '/notes',

        parse: function(resp) {
            return resp.notes;
        },

        update_lists: function() {
            this.fetch({
                'success': function() {
                    app.notes.trigger('update');
                }
            });
        }
    });

    app.notes = new Notes();
}());
