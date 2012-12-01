var app = app || {};

(function() {
    'use strict';

    var Workspace = Backbone.Router.extend({
        routes: {
            'note/:note_id': 'fetch_note'
        },

        fetch_note: function(note_id) {
            app.current_id = note_id.trim() || '';
            /* fire it */
            app.notes.trigger('update');
        }
    });

    app.Routers = new Workspace();
    Backbone.history.start();
}());
