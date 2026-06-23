# Cross-Dataset Comparison

Datasets compared: facebook_ads.csv, facebook_posts.csv, twitter_posts.csv

## Column overlap

- **Shared by all 3 datasets (27):** advocacy_msg_type_illuminating, attack_msg_type_illuminating, covid_topic_illuminating, cta_msg_type_illuminating, economy_topic_illuminating, education_topic_illuminating, engagement_cta_subtype_illuminating, environment_topic_illuminating, foreign_policy_topic_illuminating, fraud_illuminating, freefair_illuminating, fundraising_cta_subtype_illuminating, governance_topic_illuminating, health_topic_illuminating, image_msg_type_illuminating, immigration_topic_illuminating, incivility_illuminating, issue_msg_type_illuminating, lgbtq_issues_topic_illuminating, military_topic_illuminating, race_and_ethnicity_topic_illuminating, safety_topic_illuminating, scam_illuminating, social_and_cultural_topic_illuminating, technology_and_privacy_topic_illuminating, voting_cta_subtype_illuminating, womens_issue_topic_illuminating

- **Unique to `facebook_ads.csv` (14):** ad_creation_time, ad_id, bylines, currency, delivery_by_region, demographic_distribution, election_integrity_Truth_illuminating, estimated_audience_size, estimated_impressions, estimated_spend, illuminating_mentions, illuminating_scored_message, page_id, publisher_platforms

- **Unique to `facebook_posts.csv` (29):** Angry, Care, Comments, Facebook_Id, Haha, Is Video Owner?, Likes, Love, Overperforming Score, Page Admin Top Country, Page Category, Post Created, Post Created Date, Post Created Time, Post Views, Sad, Shares, Sponsor Category, Sponsor Id, Sponsor Name, Total Interactions, Total Views, Total Views For All Crossposts, Type, Video Length, Video Share Status, Wow, illuminating_scored_messageelection_integrity_Truth_illuminating, post_id

- **Unique to `twitter_posts.csv` (20):** bookmarkCount, createdAt, election_integrity_Truth_illuminating, id, illuminating_scored_message, inReplyToId, isConversationControlled, isQuote, isReply, isRetweet, lang, likeCount, month_year, quoteCount, quoteId, replyCount, retweetCount, source, url, viewCount


## Shared numeric columns — summary by dataset


### `advocacy_msg_type_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.55 | 0.50 | 0.00 | 1.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.55 | 0.50 | 0.00 | 1.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.56 | 0.50 | 0.00 | 1.00 | 1.00 |

### `attack_msg_type_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.27 | 0.44 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.22 | 0.41 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.31 | 0.46 | 0.00 | 0.00 | 1.00 |

### `covid_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.02 | 0.16 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.05 | 0.22 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.01 | 0.09 | 0.00 | 0.00 | 1.00 |

### `cta_msg_type_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.57 | 0.49 | 0.00 | 1.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.13 | 0.34 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.11 | 0.31 | 0.00 | 0.00 | 1.00 |

### `economy_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.12 | 0.33 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.09 | 0.29 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.16 | 0.37 | 0.00 | 0.00 | 1.00 |

### `education_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.01 | 0.12 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.01 | 0.12 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.02 | 0.13 | 0.00 | 0.00 | 1.00 |

### `engagement_cta_subtype_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.12 | 0.33 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.09 | 0.29 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.07 | 0.25 | 0.00 | 0.00 | 1.00 |

### `environment_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.02 | 0.14 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.02 | 0.15 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.03 | 0.17 | 0.00 | 0.00 | 1.00 |

### `foreign_policy_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.01 | 0.07 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.04 | 0.19 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.04 | 0.20 | 0.00 | 0.00 | 1.00 |

### `fraud_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.01 | 0.09 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 27,304 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |

### `freefair_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.01 | 0.08 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 27,304 | 0.00 | 0.04 | 0.00 | 0.00 | 1.00 |

### `fundraising_cta_subtype_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.23 | 0.42 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.02 | 0.13 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.01 | 0.09 | 0.00 | 0.00 | 1.00 |

### `governance_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.03 | 0.16 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.03 | 0.17 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.02 | 0.15 | 0.00 | 0.00 | 1.00 |

### `health_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.11 | 0.31 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.05 | 0.22 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.06 | 0.23 | 0.00 | 0.00 | 1.00 |

### `image_msg_type_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.22 | 0.42 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.15 | 0.36 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.23 | 0.42 | 0.00 | 0.00 | 1.00 |

### `immigration_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.03 | 0.18 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.04 | 0.20 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.07 | 0.25 | 0.00 | 0.00 | 1.00 |

### `incivility_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.19 | 0.39 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.13 | 0.33 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.18 | 0.38 | 0.00 | 0.00 | 1.00 |

### `issue_msg_type_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.38 | 0.49 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.46 | 0.50 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.51 | 0.50 | 0.00 | 1.00 | 1.00 |

### `lgbtq_issues_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.00 | 0.06 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.00 | 0.06 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.00 | 0.06 | 0.00 | 0.00 | 1.00 |

### `military_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.01 | 0.07 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.01 | 0.10 | 0.00 | 0.00 | 1.00 |

### `race_and_ethnicity_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.01 | 0.11 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.02 | 0.15 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.02 | 0.12 | 0.00 | 0.00 | 1.00 |

### `safety_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.03 | 0.18 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.03 | 0.18 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.04 | 0.19 | 0.00 | 0.00 | 1.00 |

### `scam_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.07 | 0.26 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 18,060 | 0.02 | 0.14 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.01 | 0.11 | 0.00 | 0.00 | 1.00 |

### `social_and_cultural_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.11 | 0.31 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.06 | 0.24 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.05 | 0.22 | 0.00 | 0.00 | 1.00 |

### `technology_and_privacy_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.00 | 0.03 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.00 | 0.05 | 0.00 | 0.00 | 1.00 |

### `voting_cta_subtype_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.14 | 0.35 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.02 | 0.15 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.02 | 0.13 | 0.00 | 0.00 | 1.00 |

### `womens_issue_topic_illuminating`

| dataset | count | mean | std | min | median | max |
|---|---|---|---|---|---|---|
| facebook_ads.csv | 246,745 | 0.08 | 0.27 | 0.00 | 0.00 | 1.00 |
| facebook_posts.csv | 19,009 | 0.03 | 0.16 | 0.00 | 0.00 | 1.00 |
| twitter_posts.csv | 26,034 | 0.02 | 0.15 | 0.00 | 0.00 | 1.00 |

## Shared non-numeric columns — cardinality by dataset

_No shared non-numeric columns._

