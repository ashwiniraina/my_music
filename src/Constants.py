
class Constants:

	MAX_SYS_RECURSION_DEPTH = 50000

	MAX_USERS_LASTFM_1K = 968
	MAX_SONGS_LASTFM_1K = 79239
	TOTAL_USERS_LASTFM_1K = 1000
	MAX_PLAY_SESSIONS_LASTFM_1K = 519043
	MAX_USERS_30MUSIC = 37973
	MAX_SONGS_30MUSIC = 170823
	MAX_PLAY_SESSIONS_30MUSIC = 745187

	DATASET_LASTFM_1K = "dataset_lastfm_1k"
	DATASET_30MUSIC = "dataset_30music"
	MAPS_LASTFM_1K = "maps_lastfm_1k"
	MAPS_30MUSIC = "maps_30music"

	SESSION_INTERRUPTION_DURATON_IN_SECS = 800

	MIN_PLAY_SESSION_SONG_COUNT = 5
	MIN_USERS_COUNT = 10
	MIN_SONGS_COUNT = 10

	TRAINING_SET_RATIO = 0.85
	#VALIDATION_SET_RATIO = 0.2
	TEST_SET_RATIO = 0.15

	RUN_SONG2VEC_ON_ALL_SONGS = 0
	RUN_SONG2VEC_ON_USER_TRAINING_SONGS = 1
	RUN_SONG2VEC_ON_ALL_USER_SONGS = 2

	NUM_NEAREST_NEIGHBORS = 6
	SIM_THRESHOLD_FOR_HOP_DIST = 3
	DISSIM_THRESHOLD_FOR_HOP_DIST = 3
