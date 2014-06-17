App = Ember.Application.create();

App.Router.map(function() {
	this.resource('about');
	this.resource('posts',function() {
		this.resource('post', { path: ':post_id'});
	});

});



App.PostsRoute = Ember.Route.extend({
	model : function(){
		return posts;
	// you can use your blog json data that can be later formatted into posts
	// replace it with a live json api and delete the posts
	// model:function  () {
		// return $.getJSON('http://tomdale.net/api/get_recent_posts/?callback=?').then(function  (data) {
			// return data.posts.map(function  (post) {
				// post.body = post.content;
				// return post;
			// });
		// });
	// }

	}
});

App.PostRoute = Ember.Route.extend({
	model:function  (params) {
		return posts.findBy('id',params.post_id);

		// return $.getJSON('http://tomdale.net/api/get_recent_posts/?='+params.post_id + '&callback=?').this
		// data.psot.body = data.post.content;
		// return data.post;
	}
});

 App.PostController = Ember.ObjectController.extend({
 	isEditing :false,

 	actions:{
 		edit: function(){
 			this.set('isEditing',true);
 		},
 		doneEditing:function() {
 			this.set('isEditing',false);
 		}
 	}
 });

Ember.Handlebars.helper('format-date',function  (date) {
	return moment(date).fromNow();
});

var showdown = new Showdown.converter();

Ember.Handlebars.helper('format-markdown',function  (input) {
	return new Handlebars.SafeString(showdown.makeHtml(input));
});

var posts = [{
	id:'1',
	title:"Shit happens",
	author:{name:"d2h"},
	date: new Date('05-31-2014'),
	excerpt:"There are lots of places we can go to to move !!",
	body:"I want this thing off me, you are so good to me...",
	},
	{
		id:'2',
		title:"Who the fuck is alice",
		author:{name:"d2h"},
		date:new Date('06-31-2014'),
		excerpt:"There we can go to to see the movie !!",
		body:"A long list of the topics that are there around!!",
	}
];