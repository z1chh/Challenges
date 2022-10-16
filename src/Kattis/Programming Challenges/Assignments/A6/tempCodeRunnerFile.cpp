friend ostream &operator<<(ostream &strm, const Student &s)
    {
        return s.name; //+ " (" + s.id + ")";
    }