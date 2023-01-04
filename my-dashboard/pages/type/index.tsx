export interface ITwitterUser {
    name_alias: string,
    username: string,
    stalk_user: boolean,
    date_added: Date,
    created_at: Date,
    url: string,
    description: string
}

export interface IStalkingLogsheet {
    stalking_twitter_id: string,
    new_following_twitter_id: string,
    date_added: Date
}

export interface ITwitterInfoAll {
    twitter_users: Record<string, ITwitterUser>,
    stalking_logsheet: IStalkingLogsheet[]
}