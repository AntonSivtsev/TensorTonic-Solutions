SELECT u.username,
       COALESCE(r.username, 'organic') AS referrer_name
FROM user_referrals u
left JOIN user_referrals r ON u.referred_by = r.id
order by u.username
