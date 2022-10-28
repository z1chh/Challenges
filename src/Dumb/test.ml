(* NOTES *)

let reverse l =
    let rec reverse_tr l acc =
        match l with
        | []   -> acc
        | h::t -> reverse_tr t h::acc
    in
    reverse_tr l []
