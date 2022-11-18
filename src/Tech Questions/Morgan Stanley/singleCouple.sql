SELECT {RELEVANT INFO}
FROM preg P JOIN couple C
WHERE P.pregnantID = C.pregnantID
AND C.partnerID is not null